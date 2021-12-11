import { Outlet, Link } from "react-router-dom";
import Logo from "../images/slack.png";
import "./Topnav.css";

export default function Topnav(props){
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
                    {props.props ? <Link className="nav-link" to="/signout">Sign Out</Link> : null}
                    {props.props ? <Link className="nav-link-email" to="/account">{localStorage['user_email']}</Link> : null}
                    {props.props ? null : <Link className="nav-link" to="/signin">Sign In</Link>}
                </div>
            </nav>
            <Outlet />
        </div>
    )
}