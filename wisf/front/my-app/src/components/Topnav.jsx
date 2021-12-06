import { useSelector, useDispatch } from 'react-redux';
import { display_user, remove_display_user } from '../features/user/userSlice';
import { Outlet, Link } from "react-router-dom";
import Logo from "../images/slack.png";
import "./Topnav.css";

export default function Topnav(){
    const user = useSelector((state) => state.user_display.value)
    const dispatch = useDispatch()

    console.log("TOPNAV")
    console.log(user)
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
                    <Link className="nav-link" to="/signin">Sign In</Link>
                    <Link className="user-link" to="/">{user}</Link>
                </div>
            </nav>
            <Outlet />
        </div>
    )
}