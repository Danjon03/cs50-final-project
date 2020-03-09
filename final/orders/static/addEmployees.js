document.addEventListener('DOMContentLoaded', () => {
		{
		
			alert("javaScript is running");
	
	
	
		
	
	
	
			document.querySelector('#submit').onclick = () => 
			{
				alert("inside querySelector")
				if(document.querySelector("#name").value != null && document.querySelector("#username").value && document.querySelector("#password").value)
				{
					alert("You have successfully created a new employee account. You will now be redirected to the home page");
				}
		
			};
		};
});