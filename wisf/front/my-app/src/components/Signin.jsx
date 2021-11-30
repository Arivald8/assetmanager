import "./Signin.css";

export default function Signin(props){
    return(
        <div className="sign_in_form_div">
            <p className="sign_in_title">Sign In</p>
            <form className="sign_in_form" action="/">
                <input className="sign_in_email" type="email" placeholder="Example@email.com"></input>
                <input className="sign_in_password" type="password" placeholder="Password"></input>
                <button className="sing_in_submit_btn" type="submit">Sign In</button>
                <p className="sign_in_forgot_pass"><a href='#'>Forgot Password?</a></p>
            </form>
        </div>
    )
}