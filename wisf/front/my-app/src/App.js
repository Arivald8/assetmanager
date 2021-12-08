import { useSelector } from "react-redux";
import Topnav from "./components/Topnav";

export default function App(){
    let logged_in = false
    const my_user = useSelector((state) => state.user.value)
    
    if(my_user.payload == null){}else{logged_in = true}

    return(
        <div className="app_div">
            <Topnav props={logged_in}/>
        </div>
    )
}