"""Render uncluttered excerpts from saved song matching diagnostics."""
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

p=argparse.ArgumentParser()
p.add_argument('--song',type=Path,required=True)
args=p.parse_args()
out=Path(__file__).resolve().parents[1]/'assets/images/karaoke-maker'
out.mkdir(exist_ok=True)
d=json.loads((args.song/'diagnostics.json').read_text(encoding='utf-8'))
a=json.loads((args.song/'song_vocals_alignment.json').read_text(encoding='utf-8'))
words=[w for s in a['segments'] for w in s.get('words',[]) if all(k in w for k in ('word','start','end'))]
BG,FG,GRID,TEAL,GOLD,RED='#101722','#eef3fa','#334258','#65ddc6','#ffd06a','#ff9494'
plt.rcParams.update({'font.family':'DejaVu Sans','text.color':FG,'axes.labelcolor':FG,
 'xtick.color':FG,'ytick.color':FG,'svg.fonttype':'none'})
samples=[('matching-first-chorus',103,109),('matching-final-chorus',291,299)]
manifest=[]
for name,lo,hi in samples:
 ops=d['operations'][lo:hi]
 amin=min(o['asr_range'][0] for o in ops);amax=max(o['asr_range'][1] for o in ops)
 lmin=min(o['lyric_range'][0] for o in ops);lmax=max(o['lyric_range'][1] for o in ops)
 aa=[w['word'].lower() for w in words[amin:amax]]
 ll=[t for o in ops for t in o['lyric_tokens']]
 assert len(ll)==lmax-lmin
 fig,ax=plt.subplots(figsize=(10,7),facecolor=BG)
 fig.subplots_adjust(left=.17,right=.93,top=.87,bottom=.14)
 ax.set_facecolor(BG);ax.set_xlim(0,len(aa));ax.set_ylim(0,len(ll));ax.invert_yaxis()
 ax.set_xticks(np.arange(len(aa))+.5,aa,fontsize=14);ax.xaxis.tick_top()
 ax.set_yticks(np.arange(len(ll))+.5,ll,fontsize=14)
 ax.set_xticks(np.arange(len(aa)+1),minor=True);ax.set_yticks(np.arange(len(ll)+1),minor=True)
 ax.grid(which='minor',color=GRID,lw=1);ax.tick_params(which='both',length=0,pad=10)
 for s in ax.spines.values():s.set_color(GRID)
 ax.set_xlabel('ASR →',fontsize=12,labelpad=14);ax.set_ylabel('Lyrics →',fontsize=12,labelpad=18)
 for o in ops:
  x0,x1=[v-amin for v in o['asr_range']];y0,y1=[v-lmin for v in o['lyric_range']]
  color=TEAL if o['shape']=='1:1' else (GOLD if o['kind']=='match' else RED)
  if x1>x0 and y1>y0:
   ax.add_patch(Rectangle((x0,y0),x1-x0,y1-y0,facecolor=color,edgecolor=color,alpha=.23,lw=1.5))
   ax.text((x0+x1)/2,(y0+y1)/2,o['shape'],ha='center',va='center',fontsize=15,color=color,weight='bold')
  ax.annotate('',xy=(x1,y1),xytext=(x0,y0),arrowprops={'arrowstyle':'->','lw':2.5,'color':color,
   'linestyle':'-' if o['kind']=='match' else '--'})
  if o['kind']!='match':
   if x0==x1:ax.text(x1+.1,(y0+y1)/2,o['shape'],fontsize=11,va='center',color=color)
   else:ax.text((x0+x1)/2,y1-.12,o['shape'],fontsize=11,ha='center',color=color)
 for ext in ('png','svg'):fig.savefig(out/f'{name}.{ext}',dpi=160,facecolor=BG)
 plt.close(fig)
 manifest.append({'file':name+'.png','start':words[amin]['start'],'end':words[amax-1]['end'],
  'operation_indices':[lo,hi],'operations':ops})
(out/'matching-samples.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in m.items() if k!='operations'} for m in manifest],indent=2))
