import fetchAssets from './AssetView';

export default function AssetManager(){
    let assets = fetchAssets()

    console.log("debug assetmanager")
    console.log(assets)
    console.log("debug end assetmanager")

    return(
        <div className="asset-manager-div">
            <table>
                <thead>
                    <tr>
                        <th>Device Name</th>
                        <th>Device Type</th>
                        <th>Device Asset</th>
                        <th>Device Serial</th>
                        <th>Device Model</th>
                        <th>Device Location</th>
                        <th>Device IP</th>
                        <th>Device Mac</th>
                        <th>Device School</th>
                        <th>Device Notes</th>
                    </tr>
                </thead>
                <tbody>
                    <td>`${assets}`</td>
                </tbody>
            </table>
        </div>
    )
}