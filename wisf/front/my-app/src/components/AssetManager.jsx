import { makeRequest } from './ApiCaller';

export default function AssetManager(){
    let request = makeRequest(null, 'manager', 'GET')

    fetch(request).then(function(response){
        return response.json();
    }).then(function(data){
        console.log("front debug")
        data.forEach(element => console.log(element));
        console.log('front debug end')
    })

    return(
        <div className="asset-manager-div">
            
        </div>
    )
}