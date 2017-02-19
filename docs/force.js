//references:
//https://bl.ocks.org/mbostock/4062045
//https://bl.ocks.org/mbostock/950642
//http://bost.ocks.org/mike/miserables/


function gup( name ) {
  name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
  var regexS = "[\\?&]"+name+"=([^&#]*)";
  var regex = new RegExp( regexS );
  var results = regex.exec( window.location.href );
  if( results === null )
    return null;
  else
    return results[1];
}
var type = (gup("type") || "sicp").replace("/","");


var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var zoom = d3.zoom()
  .scaleExtent([0.1, 40])
  //.translateExtent([[-100, -100], [width + 90, height + 100]])
  .on("zoom", function() {
    svg.attr("transform", d3.event.transform);
});

var drag = d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended);

var color = d3.scaleOrdinal(d3.schemeCategory20);

var directed = false;

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().distance(function(d) { return 40; }))
    .force("charge", d3.forceManyBody().strength(function(d) { return type == 'dirac' ? -550: -12; }))
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("json/" + type + ".json", function(error, graph) {
  if (error) throw error;

  simulation
      .nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(graph.links);

  svg = svg.call(zoom).append("svg:g");

  // build the arrow.
  if (directed) {
    svg.append("svg:defs").selectAll("marker")
      .data(["end"])      // Different link/path types can be defined here
    .enter().append("svg:marker")    // This section adds in the arrows
      .attr("id", String)
      .attr("viewBox", "0 -5 10 10")
      .attr("refX", 15)
      .attr("refY", -1.5)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
    .append("svg:path")
      .attr("d", "M0,-5L10,0L0,5");
  }


  var link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.selectAll(".node")
      .data(graph.nodes)
    .enter().append("g")
      .attr("class", "node")
      .call(drag);
  if (directed) {
      node.call(d3.behavior.zoom().on("zoom", rescale));
  }


  node.append("circle")
      .attr("class", "node")
      .attr("r", function(d) { return Math.max(5, Math.log(d.wordcount)); })
      .attr("fill", function(d) { return color(d.group); });

  node.append("text")
      .attr("dx", 12)
      .attr("dy", ".35em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.name; });

  // source or target properties match the hovered node.
  node.on('mouseover', function(d) {
      link.style('stroke-width', function(l) {
          if (d === l.source || d === l.target)
          return 3;
          else
          return 1;
      });
  });

  // Set the stroke width back to normal when mouse leaves the node.
  node.on('mouseout', function() {
      link.style('stroke-width', 1);
  });


  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
  }
});

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
