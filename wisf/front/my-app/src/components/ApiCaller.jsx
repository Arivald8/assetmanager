function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++){
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function makeRequest(cred, url){
    const request = new Request(
        `http://127.0.0.1:8000/${url}/`,
        {
            headers: {'X-CSRFToken': csrftoken},
            method: 'POST',
            mode: 'cors',
            credentials: 'include',
            body: cred
        }
    );
    return request
}

export const csrftoken = getCookie('csrftoken');
export { makeRequest };