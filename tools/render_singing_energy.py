"""Render the measured line-final 'take' from the singing_r8 replay (no title/footer).

The checked-in trace is the actual production _frame_rms output for lyric
line 4, using the coarse line window and the released rank-8 adapter.
Its audio SHA-256 and exact frame/boundary data are retained alongside the PNG.
"""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

assets=Path(__file__).resolve().parents[1]/'assets/images/karaoke-maker'
d=json.loads((assets/'singing-energy-data.json').read_text(encoding='utf-8'))
t=np.array(d['frame_times']);e=np.array(d['frame_rms'])
BG,FG,MUTED,TEAL,GOLD,BLUE='#101722','#eef3fa','#afbed0','#65ddc6','#ffd06a','#92baff'
plt.rcParams.update({'font.family':'DejaVu Sans','text.color':FG,'axes.labelcolor':FG,
 'xtick.color':MUTED,'ytick.color':MUTED,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(12,6.6),facecolor=BG)
fig.subplots_adjust(left=.085,right=.97,top=.94,bottom=.14)
ax.set_facecolor(BG)
ax.fill_between(t,e,color=TEAL,alpha=.14)
ax.plot(t,e,lw=1.7,color=TEAL,label='Measured vocal RMS')
ax.axhline(d['threshold'],color=GOLD,ls='--',lw=1.5,label='Quiet threshold (line q15 / q85)')
ax.axvspan(d['ctc_start'],d['ctc_end'],color=BLUE,alpha=.085)
ax.axvspan(d['ctc_end'],d['singing_end'],color=GOLD,alpha=.18)
ax.axvline(d['ctc_start'],color=BLUE,ls=':',lw=1.4)
ax.axvline(d['ctc_end'],color=BLUE,ls=':',lw=1.7)
ax.axvline(d['singing_end'],color=GOLD,ls=':',lw=1.7)
selected=(t>=d['ctc_start']-.35)&(t<=d['singing_end']+.58)
top=float(e[selected].max())*1.24
ax.set_xlim(d['ctc_start']-.35,min(d['window_end'],d['singing_end']+.58));ax.set_ylim(-top*.27,top)
ax.text(d['ctc_start']+.06,top*.92,f'“{d["word"]}”',color=BLUE,fontsize=12)
ax.text(d['ctc_start']-.055,top*.70,'Word onset',rotation=90,ha='right',va='top',color=BLUE,fontsize=10)
ax.text(d['ctc_end']-.04,top*.67,'Standard CTC end',rotation=90,ha='right',va='top',color=BLUE,fontsize=10)
ax.text(d['singing_end']-.04,top*.67,'Singing-energy end',rotation=90,ha='right',va='top',color=GOLD,fontsize=10)
q=d['quiet_frame_indices'];ax.scatter(t[q],e[q],color=GOLD,s=23,zorder=5,label='First two quiet frames after CTC end')
for y,start,end,color,label in [
 (-top*.09,d['ctc_start'],d['ctc_end'],BLUE,'Standard CTC projection'),
 (-top*.21,d['ctc_start'],d['singing_end'],GOLD,'Singing-energy projection')]:
 ax.hlines(y,start,end,color=color,lw=6)
 ax.vlines([start,end],y-top*.025,y+top*.025,color=color,lw=1.5)
 ax.text(start+.06,y+top*.025,f'{label} · {end-start:.3f} s',color=color,fontsize=10,va='bottom')
ax.axhline(0,color='#43516a',lw=.7)
ax.set_yticks(ax.get_yticks()[ax.get_yticks()>=0])
ax.set_ylim(-top*.27,top)
ax.set_xlabel('Song time',labelpad=10);ax.set_ylabel('Vocal RMS amplitude',labelpad=10)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x,_:f'{int(x)//60}:{x%60:04.1f}'))
for name in ('top','right'):ax.spines[name].set_visible(False)
for name in ('left','bottom'):ax.spines[name].set_color('#43516a')
ax.legend(loc='upper right',facecolor=BG,edgecolor='none',labelcolor=FG,fontsize=9,framealpha=.9)
for ext in ('png','svg'):
 path=assets/f'singing-energy.{ext}'
 fig.savefig(path,dpi=160,facecolor=BG)
 if ext=='svg':path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
