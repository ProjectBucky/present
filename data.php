<?php
$result = mysqli_connect("localhost","root","root","bucky");

if (!$result) {
    die('Could not connect: ' . mysql_error());
}

print_r($_POST);
//get month from
$month_given=date("m",strtotime($_POST["doe"]));

// Data Entry

$month=2;
$day=1;
$base=140;

while($day<=28){

$val=rand(20,50);
$amount=$base+$val;

$sql="INSERT INTO `expenses`(`date_of_expense`, `type`, `amount`) VALUES ('2017-".$month."-".$day."','entertainmnet',".$amount.")";
$ref = $result->query($sql);
$day=$day+6;
}


//statistics
//this month's total expense
//SELECT SUM(amount) as total FROM expenses WHERE MONTH(date_of_expense)=x
/*
$sql="SELECT MONTH(date_of_expense)as month,SUM(amount) as total FROM expenses GROUP BY MONTH(date_of_expense)";
$ref = $result->query($sql);
while ($row=mysqli_fetch_assoc($ref)){
	if($row["month"]==date(m)){

		$this_month_total=$row["total"];
	}	
	else if($row["month"]==date('m')-1){

		$prev_month_total=$row["total"];
	}	



}

echo "This Month  " .$this_month_total." Prevoius   ".$prev_month_total."<br>";


//this month's expense type wise
//SELECT MONTH(date_of_expense),type,SUM(amount) as total FROM expenses WHERE MONTH(date_of_expense)=".date('m')." GROUP BY type, MONTH(date_of_expense)
$sql="SELECT MONTH(date_of_expense),type,SUM(amount) as total FROM expenses WHERE MONTH(date_of_expense)=".date('m')." GROUP BY type, MONTH(date_of_expense)";
$ref = $result->query($sql);
while ($row=mysqli_fetch_assoc($ref)){
echo $row["type"]." ".$row["total"]."<br>";}
*/


//SELECT * FROM `expenses` WHERE `date_of_expense` ='2017-02-12'
?> 

