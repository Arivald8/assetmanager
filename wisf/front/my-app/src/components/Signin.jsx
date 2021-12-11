import "./Signin.css";
import { useNavigate } from 'react-router-dom';
import { makeRequest } from './ApiCaller';

export default function Signin(){
    const navigate = useNavigate();

    function handleSubmit(e){
        e.preventDefault();
        let formData = new FormData();
        formData.append('email', e.target.email.value)
        formData.append('pass', e.target.password.value)
        let request = makeRequest(formData, 'postsignin')
    

        fetch(request).then(function(response){
            return response.json(); 
        }).then(function(data){
            if (data["Error"] === "Invalid Credentials..."){
                console.log(data)
            } else{
                localStorage.setItem("user_id", data['uid'])
                localStorage.setItem("user_email", data['user'])
                navigate('/');
                navigate(0)

            }
        });
    }
    return(
        <div className="sign_in_form_div">
            <p className="sign_in_title">Sign In</p>
            <form className="sign_in_form" encType="" onSubmit={handleSubmit}>
                <input className="sign_in_email" type="email" name="email" placeholder="Example@email.com"></input>
                <input className="sign_in_password" type="password" name="password" placeholder="Password"></input>
                <button className="sing_in_submit_btn" type="submit">Sign In</button>
                <p className="sign_in_forgot_pass"><a href='/'>Forgot Password?</a></p>
            </form>
        </div>
    )
}
