import "./AssetManager.css";
import fetchAssets from './AssetView';
import { useState, useEffect, setState } from "react";

export default function AssetManager(){
    const [assetstate, setAssetstate] = useState(0);
    useEffect(() => {
        let isMounted = true;
        const resp = fetchAssets();
        resp.then(function(data){
            if (isMounted) setAssetstate(data);
        })
        return () => {isMounted = false};
    }, []);

    console.log("ASADASD")
    console.log(assetstate.results)

    return(
        <div className="asset-manager-div">
            <div className="manager-body">
                <div className="search-bar">
                    <form className="search-bar-form">
                        <input type="text" className="search-input"/>
                        <button className="search-submit" type="submit">Search</button>
                    </form>
                </div>
                <table className="asset-table">
                    <thead className="table-head">
                        <tr className="table-row">
                            <th className="table-header">Device Name</th>
                            <th className="table-header">Device Type</th>
                            <th className="table-header">Device Asset</th>
                            <th className="table-header">Device Serial</th>
                            <th className="table-header">Device Model</th>
                            <th className="table-header">Device Location</th>
                            <th className="table-header">Device IP</th>
                            <th className="table-header">Device Mac</th>
                            <th className="table-header">Device School</th>
                            <th className="table-header">Device Notes</th>
                        </tr>
                        {assetstate.results.map((element) => {
                            return (
                                <tdbody className="table-body">
                                    <td className="table-data">{element.device_name}</td>
                                    <td className="table-data">{element.device_type}</td>
                                    <td className="table-data">{element.device_asset}</td>
                                    <td className="table-data">{element.device_serial}</td>
                                    <td className="table-data">{element.device_model}</td>
                                    <td className="table-data">{element.device_location}</td>
                                    <td className="table-data">{element.device_ip}</td>
                                    <td className="table-data">{element.device_mac}</td>
                                    <td className="table-data">{element.device_school}</td>
                                    <td className="table-data">{element.device_notes}</td>
                                </tdbody>
                            )
                        })}
                    </thead>

                </table>
            </div>

            <div className="bottom-controls">
                <button className="add-asset-btn">Add</button>
            </div>
        </div>
    )
}