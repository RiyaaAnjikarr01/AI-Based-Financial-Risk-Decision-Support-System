const incomeChart = document.getElementById("incomeChart");

if(incomeChart){

new Chart(incomeChart,{

type:'bar',

data:{
labels:["Low","Medium","High"],
datasets:[{
label:"Income Distribution",
data:[10,25,15],
backgroundColor:["#3498db","#2ecc71","#e74c3c"]
}]
}

});

}

const debtChart = document.getElementById("debtChart");

if(debtChart){

new Chart(debtChart,{

type:'pie',

data:{
labels:["Low Debt","Medium Debt","High Debt"],
datasets:[{
data:[12,20,8],
backgroundColor:["#1abc9c","#f1c40f","#e74c3c"]
}]
}

});

}