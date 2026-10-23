/* PlainAgri site demos: calculators, diagnosis walk, zoom. Marketing demos of the app's features; no network, no storage. */
(function(){
  var D=window.PA_DATA; if(!D) return;
  function el(t,a,h){var e=document.createElement(t);if(a)for(var k in a){if(k==='class')e.className=a[k];else e.setAttribute(k,a[k]);}if(h!==undefined)e.innerHTML=h;return e;}
  function cites(ids){return ids.map(function(i,n){var r=D.sources[i];return r?'<button type="button" class="cite" data-cite="src:'+i+'" aria-label="Open source: '+r.title.replace(/"/g,'')+'">'+(n+1)+'</button>':''}).join(' ');}
  function fmt(n,d){return Number(n).toLocaleString('en-US',{maximumFractionDigits:d||0});}
  function human(id){var t=id.replace(/-/g,' ');return t.charAt(0).toUpperCase()+t.slice(1);}

  // ---------- Calculators ----------
  var cd=document.getElementById('calc-demo');
  if(cd){
    var ids=['rainwater-harvest','planting-date'], cur=ids[0];
    function compute(id,v){
      if(id==='rainwater-harvest'){
        var coll=v.roofAreaM2*v.rainfallMm*v.runoffCoeff, tank=v.dailyUseL*v.dryDays, pct=Math.min(100,coll/tank*100);
        return [['Water collected',fmt(coll)+' litres'],['Tank to cover the dry spell',fmt(tank)+' litres'],['Share of tank filled by this rain',fmt(pct)+' percent']];
      }
      var need=v.daysToMaturity+v.bufferDays, d=new Date(v.harvestDate+'T12:00:00Z'); if(isNaN(d)) return [['Sow by','Enter a valid date']];
      d.setUTCDate(d.getUTCDate()-need);
      return [['Days needed',fmt(need)+' days'],['Sow by',d.toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric',timeZone:'UTC'})]];
    }
    function draw(){
      var c=D.calculators[cur], vals={};
      cd.innerHTML='';
      var tabs=el('div',{class:'zones',role:'tablist','aria-label':'Calculator'});
      ids.forEach(function(i){var b=el('button',{type:'button',role:'tab','aria-selected':i===cur,'aria-pressed':i===cur},D.calculators[i].title);b.onclick=function(){cur=i;draw();};tabs.appendChild(b);});
      cd.appendChild(tabs);
      cd.appendChild(el('p',null,c.summary));
      var form=el('div',{class:'fields'}), out=el('div',{class:'out','aria-live':'polite'}), note=el('p',{class:'est'});
      c.inputs.forEach(function(inp){
        var id='f-'+inp.id, wrap=el('div',{class:'field'});
        wrap.appendChild(el('label',{for:id},inp.label+(inp.unit&&inp.unit!=='date'&&inp.unit!=='ratio'?' ('+inp.unit+')':'')));
        var i=el('input',{id:id,type:inp.type==='date'?'date':'number',value:inp.default,inputmode:'decimal'});
        if(inp.type!=='date'){i.min=inp.min;i.max=inp.max;i.step=inp.step;}
        vals[inp.id]=inp.type==='date'?inp.default:Number(inp.default);
        i.oninput=function(){
          if(inp.type==='date'){vals[inp.id]=i.value;}
          else{var n=parseFloat(i.value); if(isNaN(n)) n=inp.default; var cl=Math.min(inp.max,Math.max(inp.min,n)); vals[inp.id]=cl; note.textContent=cl!==n?inp.label+' adjusted to the allowed range ('+inp.min+' to '+inp.max+').':'';}
          show();
        };
        wrap.appendChild(i);
        if(inp.note) wrap.appendChild(el('small',null,inp.note));
        form.appendChild(wrap);
      });
      function show(){out.innerHTML=compute(cur,vals).map(function(r){return '<div class="stat"><div class="label">'+r[0]+'</div><div class="num">'+r[1]+'</div></div>';}).join('');}
      cd.appendChild(form); cd.appendChild(note); cd.appendChild(out);
      cd.appendChild(el('h3',null,'The formula'));
      cd.appendChild(el('ul',{class:'tick'},c.formula.map(function(f){return '<li>'+f+'</li>';}).join('')));
      cd.appendChild(el('p',{class:'est'},'Assumptions: '+c.assumptions.join(' ')+' '+c.notes.join(' ')));
      cd.appendChild(el('p',null,'Sources '+cites(c.sources)));
      show();
    }
    draw();
  }

  // ---------- Diagnosis walk ----------
  var dd=document.getElementById('diag-demo');
  if(dd){
    var T=D.tree, path=[T.start];
    function drawD(){
      var id=path[path.length-1], n=T.nodes[id]; dd.innerHTML='';
      dd.appendChild(el('p',{class:'est'},'Step '+path.length+' of this walk. '+T.title+'.'));
      if(n.q){
        dd.appendChild(el('h3',{id:'dq',tabindex:'-1'},n.q));
        var opts=el('div',{class:'opts',role:'group','aria-labelledby':'dq'});
        n.options.forEach(function(o){var b=el('button',{type:'button',class:'btn ghost'},o.label);b.onclick=function(){path.push(o.next);drawD();document.getElementById(T.nodes[o.next].q?'dq':'dr').focus();};opts.appendChild(b);});
        dd.appendChild(opts);
      }else{
        var r=n.result;
        dd.appendChild(el('h3',{id:'dr',tabindex:'-1'},(r.confidence==='likely'?'Likely cause: ':'Possible causes: ')+r.likely.map(human).join(', ')));
        dd.appendChild(el('p',null,'<b>Check:</b> '+r.check));
        dd.appendChild(el('p',null,'<b>Do:</b>')); dd.appendChild(el('ul',{class:'tick'},r.do.map(function(x){return '<li>'+x+'</li>'}).join('')));
        dd.appendChild(el('p',null,'<b>Avoid:</b>')); dd.appendChild(el('ul',{class:'tick'},r.avoid.map(function(x){return '<li>'+x+'</li>'}).join('')));
        dd.appendChild(el('p',null,'Sources '+cites(r.sources)));
        dd.appendChild(el('p',{class:'est'},'These are likely or possible causes, not a certainty. Check product labels and local rules before using any input.'));
      }
      var nav=el('p');
      if(path.length>1){var bk=el('button',{type:'button',class:'btn ghost'},'Back');bk.onclick=function(){path.pop();drawD();};nav.appendChild(bk);}
      if(path.length>1){var rs=el('button',{type:'button',class:'btn ghost'},'Start over');rs.onclick=function(){path=[T.start];drawD();};nav.appendChild(rs);}
      dd.appendChild(nav);
    }
    drawD();
  }

  // ---------- Zoom demo (marketing demo of the app's A- / A+ feature) ----------
  var zd=document.getElementById('zoom-demo');
  if(zd){
    var pct=100, view=zd.querySelector('.zview'), lab=zd.querySelector('.zpct'), minus=zd.querySelector('[data-z=minus]'), plus=zd.querySelector('[data-z=plus]');
    function step(dir){var s=(pct>=200&&dir>0)||(pct>200&&dir<0)?25:10; pct=Math.max(50,Math.min(300,pct+dir*s)); apply();}
    function apply(){zd.style.fontSize=(15*pct/100)+'px';view.classList.toggle('wide',pct>=250);lab.textContent=pct+'%';minus.disabled=pct<=50;plus.disabled=pct>=300;}
    minus.onclick=function(){step(-1)};plus.onclick=function(){step(1)};lab.onclick=function(){pct=100;apply();};
    apply();
  }
})();
