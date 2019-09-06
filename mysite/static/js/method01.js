//****************针对第一种方式的具体js实现部分******************//
//****************所使用的数据是city.js******************//

/*根据id获取对象*/
function $(str) {
    return document.getElementById(str);
}

//var addrShow = $('addr-show');
//var btn = document.getElementsByClassName('met1')[0];
var prov = $('prov');
var city = $('city');
var country = $('country');


/*用于保存当前所选的省市区*/
var current = {
    prov: '',
    city: '',
    country: ''
};

/*自动加载省份列表*/
(function showProv() {
    //btn.disabled = true;
    var len = provice.length;
    for (var i = 0; i < len; i++) {
        var provOpt = document.createElement('option');
        provOpt.innerText = provice[i]['name'];
        provOpt.value = i;
        prov.appendChild(provOpt);
    }
})();

/*根据所选的省份来显示城市列表*/
function showCity(obj) {
    var val = obj.options[obj.selectedIndex].value;
    if (val != current.prov) {
        current.prov = val;
        //addrShow.value = '';
        //btn.disabled = true;
    }
    //console.log(val);
    if (val != null) {
        city.length = 1;
        var cityLen = provice[val]["city"].length;
        for (var j = 0; j < cityLen; j++) {
            var cityOpt = document.createElement('option');
            cityOpt.innerText = provice[val]["city"][j].name;
            cityOpt.value = j;
            city.appendChild(cityOpt);
        }
    }
}

/*根据所选的城市来显示县区列表*/
function showCountry(obj) {
    var val = obj.options[obj.selectedIndex].value;
    current.city = val;
    if (val != null) {
        country.length = 1; //清空之前的内容只留第一个默认选项
        var countryLen = provice[current.prov]["city"][val].districtAndCounty.length;
        if(countryLen == 0){
            //addrShow.value = provice[current.prov].name + '-' + provice[current.prov]["city"][current.city].name;
            return;
        }
        for (var n = 0; n < countryLen; n++) {
            var countryOpt = document.createElement('option');
            countryOpt.innerText = provice[current.prov]["city"][val].districtAndCounty[n];
            countryOpt.value = n;
            country.appendChild(countryOpt);
        }
    }
}

/*选择县区之后的处理函数*/
/*function selecCountry(obj) {
    current.country = obj.options[obj.selectedIndex].value;
    if ((current.city != null) && (current.country != null)) {
        btn.disabled = false;
    }
}*/

/*点击确定按钮显示用户所选的地址*/
function showAddr() {
	//current.country = obj.options[obj.selectedIndex].value;
	var myselect=document.getElementById("prov");
	var myselect01=document.getElementById("city");
	var myselect02=document.getElementById("country");
	var myselect03=document.getElementById("di");
	var str_pro=myselect.options[myselect.selectedIndex].text
	var str_city=myselect01.options[myselect01.selectedIndex].text
	var str_country=myselect02.options[myselect02.selectedIndex].text
	var str_di=myselect03.options[myselect03.selectedIndex].text//快递信息
	var str_jd=document.getElementById("addr-show02").value//街道
	var str_name=document.getElementById("name").value//姓名
	var str_tel=document.getElementById("tel").value//电话号码
	addrShow =str_pro+"--"+str_city+"--"+str_country+"--"+str_jd;	
	document.getElementById("addr-show_02").value=addrShow
	if(str_jd !=''&&str_name!=''&&str_tel!=''&&str_di!=''){
		alert("下单成功！请到销售服务部打印快递单！\n地址为:"+addrShow+"  收件人："+document.getElementById("name").value+"  电话："+document.getElementById("tel").value+"  快递公司:"+str_di);
		document.getElementById("ac").submit();
		document.getElementById("ac——01").submit();
		if(!window.localStorage){
			alert("浏览器不支持localstorage");
		}else{
		var storage=window.localStorage;
		var name_01=document.getElementById("name01").value;
		var tel_01=document.getElementById("tel01").value;
		var bumen_01=document.getElementById("bumen").options[document.getElementById("bumen").selectedIndex].text
		var obj_01=document.getElementById("obj").options[document.getElementById("obj").selectedIndex].text
		storage.name=name_01;	
		storage.tel=tel_01;
		storage.bumen=bumen_01;
		storage.obj=obj_01;
		//alert("下单成功！请到销售服务部打印快递单!");
		
		}
	}
	else{
		//addrShow.value='';
		alert("请检查地址是否完整！和选择正确的快递公司！")
		//location.replace(location.href);
		//return;
		
	}
		
	
    //addrShow.value = provice[current.prov].name + '-' + provice[current.prov]["city"][current.city].name + '-' + provice[current.prov]["city"][current.city].districtAndCounty[current.country]+'-'+document.getElementById("addr-show02").value;
}


function offten(){
	
	 var sel = document.getElementById("prov");
	 sel.options[0].text='安徽省';
	 //alert('有两个地址')
}

function choicsAddr(){
	window.open ("Addr.html", "常用地址", "height=window.screen.height/2, width=window.screen.width/2, top=window.screen.availHeight /2, left=window.screen.width/2;, toolbar=yes, menubar=yes, scrollbars=yes, resizable=yes,location=no, status=no")
}









