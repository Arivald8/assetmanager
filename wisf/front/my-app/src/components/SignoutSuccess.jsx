export default function SignoutSuccess(props){
    localStorage.removeItem('user_email')
    localStorage.removeItem('user_id')
    console.log("This never gets executed")
    return(
        <div className="sign_out_div">
            <p className="sign_out_title">{props.user_data}</p>
            <p>TEST</p>
        </div>
    )
}