import { Outlet, Link } from "react-router-dom";
import Logo from "../images/slack.png";
import "./Topnav.css";

export default function Topnav(){
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
                    <Link className="nav-link" to="/signin">Sign In</Link>
                </div>
            </nav>
            <Outlet />
        </div>
    )
}