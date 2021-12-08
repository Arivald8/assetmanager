import { useSelector, useDispatch } from 'react-redux';
import { Outlet, Link } from "react-router-dom";
import Logo from "../images/slack.png";
import "./Topnav.css";

export default function Topnav(){
    let logged_in = false
    console.log(logged_in)
    const users = useSelector((state) => state.user.value)
    console.log("yese")
    console.log(users.payload)
    if(users.payload == null){}else{logged_in = true}

    console.log("TOPNAV")
    console.log(users.payload)
    console.log(logged_in)
    console.log("TOPNAV")

    return(
        <div className="top-nav-div">
            <nav className="nav-nav">
                <div className="left-nav">
                    <div className="left-nav-logo-div">
                        <img className="nav-logo-img" src={Logo} alt="Logo"></img>
                    </div>
                </div>
                <div className="right-nav">
                    <Link className="nav-link" to="/">Home</Link>
                    {logged_in ? <Link className="nav-link" to="/signout">Sign Out</Link> : null}
                    {logged_in ? <Link className="nav-link-email" to="/account">{users.payload}</Link> : null}
                    {logged_in ? null : <Link className="nav-link" to="/signin">Sign In</Link>}
                </div>
            </nav>
            <Outlet />
        </div>
    )
}