import "./AssetManager.css";
import fetchAssets from './AssetView';

export default function AssetManager(){
    let assets = fetchAssets()

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
                    </thead>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>
                    <tbody className="table-body">
                        <td className="table-data">KHS-T-125</td>
                        <td className="table-data">Laptop</td>
                        <td className="table-data">123456</td>
                        <td className="table-data">abc123</td>
                        <td className="table-data">g10</td>
                        <td className="table-data">KHS IT office</td>
                        <td className="table-data">123.456</td>
                        <td className="table-data">adbj2a</td>
                        <td className="table-data">khs</td>
                        <td className="table-data">very good</td>
                    </tbody>     
                </table>
            </div>

            <div className="bottom-controls">
                <button className="add-asset-btn">Add</button>
            </div>
        </div>
    )
}