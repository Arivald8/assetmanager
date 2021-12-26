import { useEffect } from 'react';
import { useState } from 'react';
import { makeRequest } from './ApiCaller';

export default function FetchAssets(){
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState([]);

    let request = makeRequest(null, 'manager/view-assets', 'GET')

    useEffect(() => {
        fetch(request)
            .then(res => res.json())
            .then(
                (paginator_obj) => {
                    console.log("debug here")
                    console.log(paginator_obj)
                    console.log("debug end here")
                    setIsLoaded(true);
                    setItems(paginator_obj);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [])

    if (error) {
        return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
        return <div>Loading...</div>;
    } else {
        return (
            <div className='asset-table-div'>
                <table className='asset-table'>
                    <thead className='table-head'>
                        <tr className='table-row'>
                            <th className='table-data'>Name</th>
                            <th className='table-data'>Type</th>
                            <th className='table-data'>Asset</th>
                            <th className='table-data'>Serial Number</th>
                            <th className='table-data'>Model Number</th>
                            <th className='table-data'>IP</th>
                            <th className='table-data'>Mac</th>
                            <th className='table-data'>Location</th>
                            <th className='table-data'>School</th>
                            <th className='table-data'>Notes</th>
                        </tr>
                    </thead>
                    <tbody>
                    {items.results?.map(item => (
                        <tr className='table-row'>
                            <td className='table-data'>
                                {item.device_name}
                            </td>
                            <td className='table-data'>
                                {item.device_type}
                            </td>
                            <td className='table-data'>
                                {item.device_asset}
                            </td>
                            <td className='table-data'>
                                {item.device_serial}
                            </td>
                            <td className='table-data'>
                                {item.device_model}
                            </td>
                            <td className='table-data'>
                                {item.device_ip}
                            </td>
                            <td className='table-data'>
                                {item.device_mac}
                            </td>
                            <td className='table-data'>
                                {item.device_location}
                            </td>
                            <td className='table-data'>
                                {item.device_school}
                            </td>
                            <td className='table-data'>
                                {item.device_notes}
                            </td>
                        </tr>
                    ))}

                    </tbody>
                </table>

            </div>
        );
    }
}

