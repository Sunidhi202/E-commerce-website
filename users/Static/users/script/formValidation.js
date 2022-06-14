console.log("Working")

const firstName = document.getElementById('firstName');
const lastName = document.getElementById('lastName');
const email = document.getElementById('userEmail');
const password1 = document.getElementById('pass1');
const password2 = document.getElementById('pass2');

const invalidClass = document.getElementById('validationMsg');

firstName.addEventListener('blur', () =>{
    console.log(invalidClass.innerHTML);
    if (password1.value !== password2.value){
        
    }
    // if (firstName.value===""){
    //     console.log("This field is required");
    //     invalidClass.innerHTML = "<li>This field is required</li>";
    //     firstName.classList.add("is-invalid");
    // }
    // else{
    //     firstName.classList.remove("is-invalid")
    // }
})

function verifyPassword(password){

    if(password == ""){
        return 0;
    }

    if(password.length < 8){
        return 0;
    }

    if(password.length > 15){
        return 0;
    }

}