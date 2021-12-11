import Topnav from "./components/Topnav";
import Sidenav from "./components/Sidenav";

export default function App(){
    let logged_in = false
    
    if (localStorage['user_email']){logged_in = true}
    console.log(localStorage)
    console.log(logged_in)

    return(
        <div className="app_div">
            <Topnav props={logged_in}/>
            {logged_in ? <Sidenav /> : null}
        </div>
    )
}