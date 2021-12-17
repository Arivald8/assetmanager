import { Link } from "react-router-dom";
import "./Sidenav.css"; 

export default function Sidenav(props){
    return(
        <div className="side-nav-div">
            <p className="side-nav-title">Navigator</p>
            <Link className="side-nav-link" to="/asset-manager">Asset Manager</Link>
            <Link className="side-nav-link" to="/">Device Allocation</Link>
            <Link className="side-nav-link" to="/">Admin Dashboard</Link>
        </div>
    )
}