import "./Signin.css";

export default function Signin(props){
    function getCookie(name){
        let cookieValue = null;
        if (document.cookie && document.cookie !== ''){
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++){
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')){
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    let handleSubmit = (e) => {
        e.preventDefault();
        let formData = new FormData();
        formData.append(e.target.email.value, e.target.password.value)
        let credentials = {
            "email": e.target.email.value,
            "password": e.target.password.value
        }
        console.log("DEBUG===========")
        console.log(credentials['email'])
        sendSubmit(formData)
    }

    let sendSubmit = (cred) => {
        console.log("sendSubmit herere")
        for (let pair of cred.entries()){
            console.log(pair[0]+ ', '+ pair[1]);
        }
        const request = new Request(
            'http://127.0.0.1:8000/postsignin/',
            {
                headers: {'X-CSRFToken': csrftoken},
                method: 'POST',
                mode: 'cors',
                credentials: 'include',
                body: 'hello world'
            }
        );
        console.log("after request was made")
        console.log(request)
        console.log(request.body)
        fetch(request).then(function(response){
            console.log("DEBUG")
            console.log(response)
        })

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
