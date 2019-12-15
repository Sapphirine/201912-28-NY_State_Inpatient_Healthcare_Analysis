function MapView(topology, values) {
  var width = 1960, height = 800;
  var svg = d3.select("#heatmap")
              .append("svg")
              .attr("width", width)
              .attr("height", height);

  var geojson = topojson.feature(topology, topology.objects.cb_2015_new_york_county_20m);

  var bounds = d3.geo.bounds(geojson), center = d3.geo.centroid(geojson);
  var projection = d3.geo.mercator().translate([width / 2, height / 2]);
  var distance = d3.geo.distance(bounds[0], bounds[1]);

  var scale = height / distance / Math.sqrt(1.1);
  projection.scale(scale).center(center);

  var path = d3.geo.path().projection(projection);

  Array.prototype.max = function() {
    return Math.max.apply(null, this);
  };

  Array.prototype.min = function() {
    return Math.min.apply(null, this);
  };

  var max = Math.max.apply(null, Object.values(values));
  var min = Math.min.apply(null, Object.values(values));

  var colorMap = d3.scale.linear()
                   .range(["blue", "white", "red"])
                   .domain([min, 0, max])

  var div = d3.select("body").append("div")
              .attr("class", "tooltip")
              .style("opacity", 0);

  svg.selectAll("path")
     .data(geojson.features)
     .enter().append("path")
     .attr("d", path)
     .forEach( function(d, i) { 
       d.forEach( function(d2, i2) {
          $(d2).css({'fill': colorMap(values[geojson.features[i2].properties.NAME])}); 
       })
     });

  svg.selectAll("path")
     .on("mouseover", function(d) {
        div .transition()
            .duration(200)
            .style("opacity", .9);
        div .html(d.properties.NAME + " : " + values[d.properties.NAME])
            .style("left", (d3.event.pageX) + "px")
            .style("top", (d3.event.pageY - 5) + "px");
     })
    .on("mouseout", function(d, i) {
        div .transition()
            .duration(200)
            .style("opacity", 0);
        div .html('')
            .style("left", "0px")
            .style("top", "0px");   
    });
};

function updateChoice() {
  $("#id_field2_choice").change(function () {
    var url = $("#heatmapForm").attr("data-group-url");  // get the url of the `load_dependnts` view
    var category = $(this).val() || '-----';             // get the selected country ID from the HTML input
    console.log(url)
    console.log(category)
    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'category': category       // add the country id to the GET parameters
      },
      success: function (data) {   // data is the return of the `load_cities` view function
        $("#id_field3_choice").html(data);
        $("#id_field4_choice").html(data);  // replace the contents of the group input
      }
    });
  });
}
