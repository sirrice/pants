---
layout: layout
---

<script type="text/javascript">
  var arr = [
    {% for d in {{site.data.dudes}} %}
      ['{{d.name}}',{{d.pk}}]
      {%if {{forloop.last}} == false %},{%endif%}
    {%endfor%}];
  var suffixes = ["undies", "pants", "nopants", "hi", "bye"];
  var dudeidx = 0;
  function loadarr() {
    if (dudeidx < 0 || dudeidx >= arr.length) return;
    var pair = arr[dudeidx];
    prefix = pair[0];
  	for (suffix in suffixes) {
  		suffix = suffixes[suffix];
        var val = ["./files/images/",prefix, "_", suffix, ".png"].join("");
  		$("#" + suffix).attr("src", val);
  		$("#" + suffix).hide();
  	}  	
  	$("#undies").show();
	var nextprefix = arr[(dudeidx+1) % arr.length][0];
	var prevprefix = arr[(dudeidx+arr.length-1) % arr.length][0];
	$("#nextimg").attr("src", ["./files/images/", nextprefix, "_preview.png"].join(""));
	$("#previmg").attr("src", ["./files/images/", prevprefix, "_preview.png"].join(""));
	
	// check if I've voted
	$("#shownuts").removeClass(); $("#showpants").removeClass();
	$.get("/" + pair[1] + "/", {}, function(data) {
		if (data.vote == 1)
			$("#showpants").addClass("voted");
		else if (data.vote == -1)
			$("#shownuts").addClass("voted");
	}, "json");
	
	
  }

  $(document).ready(function(){
  	$("#shownuts").hover(function(){$("#undies").hide(); $("#nopants").show();}, 
  						function(){$("#nopants").hide(); $("#undies").show();});
  	$("#showpants").hover(function(){$("#undies").hide(); $("#pants").show();}, 
  						function(){$("#pants").hide(); $("#undies").show();});
  	$("#hello").hover(function(){$("#undies").hide(); $("#hi").show();}, 
  						function(){$("#hi").hide(); $("#undies").show();});		
  	$("#thanks,#mylink").hover(function(){$("#undies").hide(); $("#bye").show();}, 
  						function(){$("#bye").hide(); $("#undies").show();});	
  	$("#next").click(function(){dudeidx = (dudeidx+1) % arr.length; loadarr();});
  	$("#prev").click(function(){dudeidx = (dudeidx+arr.length-1) % arr.length; loadarr();});
  	loadarr();
		
	$(document).keydown(function(e) {
        switch (e.which) {
          case 39:
            dudeidx = (dudeidx+1) % arr.length; loadarr();
            break;
          case 37:
            dudeidx = (dudeidx+arr.length-1) % arr.length; loadarr();
            break;
        }
    });
  });

</script>  


<div style="position:relative;">



<div id="next">
    <img class="navimg" id="nextimg"/>
</div>
<div id="prev">
    <img class="navimg" id="previmg"/>
</div>


<div class="msgdiv" >
<span id="hello">You there!</span><br/>
<a href="#" id="showpants">Pants</a> or <a href="#" id="shownuts">No Pants</a>?<br/>
<span id="thanks">Thanks</span>!
<!--<button id="showpants" style="margin-left:2em;" >Pants!</button> <span>or</span> <button id="shownuts">No Pants!</button>-->
</div>
<!--<div class="info">hover to see, click to vote, arrow keys to see next/prev!</div>-->
<div class="img" id="picture"  >
<img class="dude" id="undies" />
<img class="dude" id="pants" />
<img class="dude" id="nopants" />
<img class="dude" id="hi" />
<img class="dude" id="bye" />
</div>
</div>
