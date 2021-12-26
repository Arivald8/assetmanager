import "./AssetManager.css";
import FetchAssets from './AssetView';
import { useState, useEffect, setState } from "react";


export default function AssetManager(){
    return(
        <div className="asset-manager-div">
            <div className="search-bar">
                <form className="search-bar-form">
                    <input type="text" className="search-input"/>
                    <button className="search-submit" type="submit">Search</button>
                </form>
            </div>
            <div className="manager-body">
                <FetchAssets />
            </div>

            {/*
            <div className="manager-body">
                <div className="search-bar">
                    <form className="search-bar-form">
                        <input type="text" className="search-input"/>
                        <button className="search-submit" type="submit">Search</button>
                    </form>
                </div>
                <FetchAssets />
            </div>

            <div className="bottom-controls">
                <button className="add-asset-btn">Add</button>
            </div>
            */}

        </div>
    )
}