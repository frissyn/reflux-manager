javascript:function reflux(e){if(null==e||""==e)alert("Given referral code is empty or null.");else{fetch("https://api.reflux.repl.co/theme/"+e).then(e=>e.json()).then(e=>{if(confirm(`Name: ${e.name} \n`+`Author: ${e.author.name} \n`+`Description: ${e.description} \n`+`Downloads: ${e.downloads}  \n\n`+"Load this theme?")){let t=document.getElementById("reflux-target");t||(t=document.createElement("style")),t.type="text/css",t.id="reflux-target",t.textContent=e.stylesheet,document.getElementsByTagName("head")[0].appendChild(t),alert(`Loaded '${e.name}' into Replit, enjoy!`)}}).catch(e=>alert("Couldn't load theme.\n"+e))}}reflux("54caf074322a8f39");