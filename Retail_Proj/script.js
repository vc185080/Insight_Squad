document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();

  var emailId = document.getElementById('emailId').value;
  var password = document.getElementById('password').value;

  if (emailId === 'loyaltyuser@gmail.com' && password === 'password') {

    window.location.href = `Customer.html?username=${encodeURIComponent("Loyalty User")}`;
    // Perform further actions after successful login
  } 
  else if(emailId === 'newuser@gmail.com' && password === 'password'){
    window.location.href = `Customer.html?username=${encodeURIComponent("New User")}`;
  }
  else {
    var errorElement = document.createElement('p');
    errorElement.className = 'error';
    errorElement.textContent = 'Invalid username or password';
    errorElement.style = "text-align:center; color:white;"
    document.getElementById('loginForm').appendChild(errorElement);
  }
});
