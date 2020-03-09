document.addEventListener('DOMContentLoaded', () => {
		
		var items = [];
		var quantities = [];
		
		
		table = document.getElementById("#table");
		
		
		//codes
		for(var i=0;i <= 5; i++)
		{
			
			alert(document.getElementById("table").rows[i].cells.namedItem("myTr").innerHTML);
				
				alert("inside loop");
		}
		
		
	
	
	
			
});