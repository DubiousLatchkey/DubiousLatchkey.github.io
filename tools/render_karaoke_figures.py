"""Render source-based portfolio figures. Requires matplotlib, numpy, rapidfuzz.

Run using the karaoke-maker venv; --source points at that repository.
The energy trace is explicitly synthetic; matcher operations use the real code.
"""
import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

p = argparse.ArgumentParser()
p.add_argument('--source', type=Path, required=True)
p.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'assets/images/karaoke-maker')
args = p.parse_args()
sys.path.insert(0, str(args.source))
from lyrics_matcher import GeneralizedMatcher

OUT = args.output
OUT.mkdir(parents=True, exist_ok=True)
BG, PANEL, FG, MUTED = '#101722', '#1b2738', '#eef3fa', '#afbed0'
TEAL, GOLD, BLUE = '#65ddc6', '#ffd06a', '#92baff'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'text.color': FG,
    'axes.labelcolor': FG, 'xtick.color': MUTED, 'ytick.color': MUTED,
    'axes.edgecolor': '#43516a', 'figure.facecolor': BG, 'axes.facecolor': BG,
    'font.size': 12, 'svg.fonttype': 'none'})

def base(title, subtitle, size=(14, 8)):
    fig = plt.figure(figsize=size, facecolor=BG)
    fig.text(.045, .94, title, fontsize=25, weight='bold')
    fig.text(.045, .895, subtitle, fontsize=12, color=MUTED)
    ax = fig.add_axes([.035, .06, .93, .79])
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')
    return fig, ax

def box(ax, x, y, w, h, title, detail='', color=TEAL):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.5,rounding_size=1.8',
        facecolor=PANEL, edgecolor=color, linewidth=1.3))
    ax.text(x+2,y+h-4,title,fontsize=14,weight='bold',va='top',color=color)
    ax.text(x+2,y+h-11,detail,fontsize=11,va='top',linespacing=1.6)

def arrow(ax,a,b,color=MUTED):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='-|>',color=color,lw=1.7))

def save(fig, name):
    fig.savefig(OUT/(name+'.png'),dpi=160,facecolor=BG)
    fig.savefig(OUT/(name+'.svg'),facecolor=BG)
    plt.close(fig)

fig, ax = base('A speech model adapted to singing', 'Production release: singing_r8 · wav2vec2-base-960h + LoRA + CTC forced alignment')
box(ax,2,66,27,29,'01  Vocal audio','Mono, resampled to 16 kHz\nApproximate lyric-line window\nUp to 0.5 s context on each side')
box(ax,36,66,27,29,'02  Acoustic features','7 convolutional layers\n512 channels per layer\nFeature projection: 512 → 768',BLUE)
box(ax,70,66,28,29,'03  Transformer × 12','Hidden size 768 · 12 heads\nFrozen base weights\nTrainable LoRA on Q and V',GOLD)
arrow(ax,(29,80),(36,80)); arrow(ax,(63,80),(70,80)); arrow(ax,(84,66),(84,57))
box(ax,70,28,28,29,'04  CTC output head','Trainable linear head: 768 → 32\nCharacters + separator + blank\nFramewise log probabilities',GOLD)
box(ax,36,28,27,29,'05  Constrained path','Known lyric characters\nCTC Viterbi dynamic program\nCharacter spans → word spans',BLUE)
box(ax,2,28,27,29,'06  Singing projection','Keep CTC word starts\nExtend ends through vocal energy\nStop at quiet run / next word')
arrow(ax,(70,42),(63,42)); arrow(ax,(36,42),(29,42))
ax.text(3,15,'LoRA: ΔW = (16 / 8) BA',color=GOLD,fontsize=14,weight='bold')
ax.text(3,6,'Rank 8 · dropout 0.05 · 319,520 trainable parameters / 94,715,840 total (0.34%)',fontsize=12)
ax.text(99,6,'Gold = trained components',ha='right',color=GOLD,fontsize=11)
save(fig,'ctc-architecture')

fig, ax = base('Let a sung vowel finish', 'Singing-energy projection · illustrative synthetic trace, not a measured song segment')
plot = fig.add_axes([.09,.39,.84,.39],facecolor=BG)
t=np.arange(0,1.6,.02)
energy=np.where((t>=.18)&(t<.94),.38+.06*np.sin(t*25),.025+.005*np.cos(t*17))
energy=np.where((t>=1.22)&(t<1.5),.32+.03*np.sin(t*23),energy)
low,high=np.quantile(energy,[.15,.85]); threshold=low+.2*max(0,high-low)
lexical_end=.50; next_start=1.22
quiet=None
for i in range(int(lexical_end/.02)+1,int(next_start/.02)-1):
    if energy[i]<=threshold and energy[i+1]<=threshold: quiet=i;break
assert quiet is not None
new_end=t[quiet-1]
plot.fill_between(t,energy,color=TEAL,alpha=.15);plot.plot(t,energy,color=TEAL,lw=2,label='RMS per acoustic frame')
plot.axhline(threshold,color=GOLD,ls='--',label='Adaptive quiet threshold')
plot.axvspan(lexical_end,new_end,color=GOLD,alpha=.16)
for x,label,col in [(lexical_end,'CTC lexical end',BLUE),(new_end,'Extended word end',GOLD),(next_start,'Next word start',MUTED)]:
    plot.axvline(x,color=col,ls=':');plot.text(x+.018,.51,label,rotation=90,va='top',fontsize=10,color=col)
plot.scatter(t[quiet:quiet+2],energy[quiet:quiet+2],color=GOLD,zorder=5)
plot.set_ylim(0,.55);plot.set_xlim(0,1.6);plot.set_xlabel('Time within the example line (seconds)');plot.set_ylabel('Frame RMS');plot.spines[['top','right']].set_visible(False)
plot.legend(loc='upper left',fontsize=9,facecolor=PANEL,labelcolor=FG,framealpha=.9)
ax.text(3,29,'1. Measure energy',color=TEAL,weight='bold',fontsize=14)
ax.text(3,21,'RMS = √mean(x²) in a window\ncentered on each acoustic frame.',fontsize=11,linespacing=1.5)
ax.text(36,29,'2. Adapt to the line',color=GOLD,weight='bold',fontsize=14)
ax.text(36,21,'q15 + 0.20 × (q85 − q15)\nsets the quiet threshold.',fontsize=11,linespacing=1.5)
ax.text(70,29,'3. Extend conservatively',color=BLUE,weight='bold',fontsize=14)
ax.text(70,21,'Stop before 2 quiet frames,\nwithout crossing the next word.',fontsize=11,linespacing=1.5)
ax.text(3,5,'No quiet run? Extend to the next word boundary; for the final word, keep the original end.',fontsize=11,color=MUTED)
save(fig,'singing-energy')

asr=['we','can','not','stop','oh','an','ice','day']; lyrics=['we','cannot','stop','a','nice','day']
ops=GeneralizedMatcher().align(asr,lyrics)
(OUT/'matching-example.json').write_text(json.dumps([o.as_dict(asr,lyrics) for o in ops],indent=2)+'\n')
fig,ax=base('Match phrases, not just individual words','Actual output from the default exact global/text matcher · constructed example')
grid=fig.add_axes([.09,.21,.48,.60],facecolor=BG)
grid.set_xlim(0,len(asr));grid.set_ylim(0,len(lyrics));grid.invert_yaxis()
grid.set_xticks(np.arange(len(asr))+.5,asr,fontsize=11);grid.xaxis.tick_top()
grid.set_yticks(np.arange(len(lyrics))+.5,lyrics,fontsize=11)
grid.set_xticks(np.arange(len(asr)+1),minor=True);grid.set_yticks(np.arange(len(lyrics)+1),minor=True)
grid.grid(which='minor',color='#334258');grid.tick_params(which='both',length=0,pad=8)
grid.set_xlabel('ASR tokens consumed →',labelpad=12);grid.set_ylabel('Supplied lyric tokens consumed →',labelpad=14)
row=88
for op in ops:
    a,b=op.asr_start,op.lyric_start;c,d=op.asr_end,op.lyric_end
    col=GOLD if op.kind!='match' else (TEAL if op.shape=='1:1' else BLUE)
    if c>a and d>b:
        grid.add_patch(Rectangle((a,b),c-a,d-b,facecolor=col,alpha=.28,edgecolor=col,lw=2))
        grid.text((a+c)/2,(b+d)/2,op.shape,ha='center',va='center',weight='bold')
    grid.annotate('',xy=(c,d),xytext=(a,b),arrowprops=dict(arrowstyle='->',color=col,lw=2))
    label=' '.join(asr[a:c]) or '∅';target=' '.join(lyrics[b:d]) or '∅'
    ax.text(61,row,f'{op.shape}   {label}  →  {target}',fontsize=12,weight='bold',color=col)
    ax.text(61,row-5,f'Incremental cost: {op.cost:.2f}',fontsize=10,color=MUTED)
    row-=14
ax.text(3,3,'Blue: split/merge or resegmentation    Teal: exact 1:1    Gold: unmatched vocalization',fontsize=11,color=MUTED)
save(fig,'many-to-many')
print('Rendered architecture, singing-energy and matching figures:',OUT)
