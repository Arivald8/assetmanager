import "./App.css";
import Topnav from "./components/Topnav";
import Sidenav from "./components/Sidenav";
import AssetManager from "./components/AssetManager";

import { useLocation } from "react-router-dom";

export default function App(){
    let logged_in = false
    let asset_manager = false

    const location = useLocation();
    console.log(location.pathname)
    
    if (localStorage['user_email']){logged_in = true}
    if (location.pathname === "/asset-manager"){asset_manager = true}

    return(
        <div className="app_div">
            <Topnav props={logged_in}/>
            {logged_in ? <Sidenav /> : null}
            {asset_manager ? <AssetManager /> : null}
        </div>
    )
}