var chart;
var appliances =	[
						{% for appliance in appliances %}
							"{{appliance}}",
						{% endfor %}
					];
var user_data =		[
						{% for datum in user_data %}
						  {{datum}},
						{% endfor %}
					];
var average_data =	[
						{% for datum in average_data %}
						  {{datum}},
						{% endfor %}
					];
var normalized_user_data = [];
var normalized_average_data = [];
var total_user = 0;
var total_average = 0;
var total = 0;
var data;
var browserData;
var versionsData;
var colors = Highcharts.getOptions().colors,
	categories = ['Bathroom', 'Kitchen'],
	name = 'Browser brands';
function calculate_pie(){
	normalized_user_data = [];
	normalized_average_data = [];
	tota = 0;
	total_user = 0;
	total_average = 0;
	for(var i = 0; i<user_data.length; i++)
		total += user_data[i];
	for(var i = 0; i<average_data.length; i++)
		total += average_data[i];
	for(var i = 0; i<user_data.length; i++)
	{
		var d = Math.ceil(user_data[i]*100/total);
		normalized_user_data.push(d);
		total_user += d;
	}
	for(var i = 0; i<average_data.length; i++)
	{
		var d = Math.ceil(average_data[i]*100/total);
		normalized_average_data.push(d);
		total_average += d; 
	}
	data = [{
				y: total_user,
				color: colors[0],
				drilldown: {
					name: 'Bathroom details',
					categories: appliances, 
					data: normalized_user_data, 
					color: colors[0]
				}
			}, {
				y: total_average,
				color: colors[1],
				drilldown: {
					name: 'Kitchen details',
					categories: appliances, 
					data: normalized_average_data, 
					color: colors[1]
				}
			}];

	// Build the data arrays
	browserData = [];
	versionsData = [];
	for (var i = 0; i < data.length; i++) {

		// add browser data
		browserData.push({
			name: categories[i],
			y: data[i].y,
			color: data[i].color
		});

		// add version data
		for (var j = 0; j < data[i].drilldown.data.length; j++) {
			var brightness = 0.2 - (j / data[i].drilldown.data.length) / 5 ;
			versionsData.push({
				name: data[i].drilldown.categories[j],
				y: data[i].drilldown.data[j],
				color: Highcharts.Color(data[i].color).brighten(brightness).get()
			});
		}
	}
}
calculate_pie();


$(function(){
		$("#appliance_input").keyup(function(event){
				if(event.keyCode=="13"){
					var v = $(this).val();
					var d = "<div>" + v + "</div>";
					$("#appliance_list").append(d);

					appliances.push(v);
					user_data.push(5000);
					average_data.push(5000);
					calculate_pie();

					chart.xAxis[0].setCategories(appliances,true);
					chart.series[0].setData(user_data,true);
					chart.series[1].setData(average_data,true);

					chart2.series[0].setData(browserData,true);
					chart2.series[1].setData(versionsData,true);

					$(this).val("");
				}
			});
		chart = new Highcharts.Chart({
			chart: {
				renderTo: 'container',
				type: 'bar',
			},
			title: {
				text: 'Energy Usage Summary'
			},
			xAxis: {
				categories: appliances
			},
			yAxis: {
				title: {
					text: 'Energy Used'
				}
			},
			series: [{
				name: 'Your Current Usage',
				  data: user_data 
			}, {
				name: 'Average American Usage',
				  data: average_data 
			}]
		});
});


	var chart2;
$(function () {
	$(document).ready(function() {
	
	
		// Create the chart
		chart2 = new Highcharts.Chart({
			chart: {
				renderTo: 'personal',
				type: 'pie'
			},
			title: {
				text: 'Energy Usage Detailed'
			},
			yAxis: {
				title: {
					text: 'Total percent market share'
				}
			},
			plotOptions: {
				pie: {
					shadow: false
				}
			},
			tooltip: {
				formatter: function() {
					return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
				}
			},
			series: [{
				name: 'Rooms',
				data: browserData,
				size: '60%',
				dataLabels: {
					formatter: function() {
						return this.y > 5 ? this.point.name : null;
					},
					color: 'white',
					distance: -30
				}
			}, {
				name: 'Appliance',
				data: versionsData,
				innerSize: '60%',
				dataLabels: {
					formatter: function() {
						// display only if larger than 1
						return this.y > 1 ? '<b>'+ this.point.name +':</b> '+ this.y +'%'  : null;
					}
				}
			}]
		});
	});
	
});
