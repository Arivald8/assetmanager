import "./Signin.css";

export default function Signin(props){
    let handleSubmit = (e) => {
        e.preventDefault();
        let credentials = {
            "email": e.target.email.value,
            "password": e.target.password.value
        }
        sendSubmit(credentials)
    }

    let sendSubmit = (cred) => {
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(cred)
        };

        fetch('http://127.0.0.1:8000/postsignin/', requestOptions)
            .then(response => response.json())
            .then(data => console.log(data))

    }

    return(
        <div className="sign_in_form_div">
            <p className="sign_in_title">Sign In</p>
            <form className="sign_in_form" onSubmit={handleSubmit}>
                <input className="sign_in_email" type="email" name="email" placeholder="Example@email.com"></input>
                <input className="sign_in_password" type="password" name="password" placeholder="Password"></input>
                <button className="sing_in_submit_btn" type="submit">Sign In</button>
                <p className="sign_in_forgot_pass"><a href='#'>Forgot Password?</a></p>
            </form>
        </div>
    )
}
