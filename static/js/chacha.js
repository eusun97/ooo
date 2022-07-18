var myChart = $('#line-chart');
var myLineChart = new Chart(myChart,{
  type:'bar',
  data:{
    labels:[
      '1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월',
    ],
    datasets:[
      {
        label:'2022',
        data:[
          14,25,37,84,93,62,15,38,78,60,68,100
        ],
        backgroundColor: 'lightgray',
        borderColor: 'white',
      },
      {
        label:'2023',
        data:[
          2,16,83,49,16,36,48,100,14,79,93,72
        ],
        backgroundColor: 'skyblue',
        borderColor: 'skyblue',
      }
    ]
  }
})