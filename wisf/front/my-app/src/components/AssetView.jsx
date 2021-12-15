import { makeRequest } from './ApiCaller';

export default function fetchAssets(){
    let request = makeRequest(null, 'manager/view-assets', 'GET')

    return fetch(request).then(function(response){
        return response.json();
    }).then(function(data){
        console.log("front debug")
        console.log(data.count)
        console.log(data.previous)
        console.log(data.next)
        console.log(data.results)
        console.log('front debug end')
        return data
    })
}
