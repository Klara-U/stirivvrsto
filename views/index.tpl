<!DOCTYPE html>
<html>
<head>
<title>Štiri v vrsto</title>
<style>
h1 {
	text-align: center;
	font-family: Arial, sans-serif;
}

#gumbi {
	width: 532px;
	height: 50px;
	margin: 0 auto;
}

#gumbi .gumb {
	display: inline-block;
	float: left;
	width: 56px;
	height: 30px;
	margin: 10px;
	opacity: 0.5;
	cursor: pointer;
}
#gumbi .gumb:hover {
	opacity: 1;
}

#polje {
	background: #1f74dd;
	box-sizing: border-box;
	width: 538px;
	height: 459px;
	margin: 0 auto;
	border: 3px solid #29303a;
	border-radius: 3px 3px 0 0;
	border-width: 3px 3px 0 3px;
}

#polje .prostor {
	display: inline-block;
	float: left;
	width: 50px;
	height: 50px;
	background: white;
	border-radius: 200px;
	border: 3px solid #29303a;
	margin: 10px;
}

#polje .zeton1 {
	background: #c72f30;
}
#polje .zeton2 {
	background: #dac307;
}

#bottom {
	background: #dac307;
	box-sizing: border-box;
	width: 580px;
	height: 35px;
	margin: 0 auto;
	border: 3px solid #29303a;
	border-radius: 3px;
}
</style>
</head>
<body>

<h1>{{sporocilo}}</h1>

<div id="gumbi">
	<a href="/igraj/0"><img class="gumb" src="/img/arrow-down.svg"></a>
	<a href="/igraj/1"><img class="gumb" src="/img/arrow-down.svg"></a>
	<a href="/igraj/2"><img class="gumb" src="/img/arrow-down.svg"></a>
	<a href="/igraj/3"><img class="gumb" src="/img/arrow-down.svg"></a>
	<a href="/igraj/4"><img class="gumb" src="/img/arrow-down.svg"></a>
	<a href="/igraj/5"><img class="gumb" src="/img/arrow-down.svg"></a>
	<a href="/igraj/6"><img class="gumb" src="/img/arrow-down.svg"></a>
</div>

<div id="polje">
	{{!polje}}
</div>
<div id="bottom"></div>

</body>
</html>