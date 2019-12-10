import React from 'react'

const Warehouses = ({ warehouses }) => {
    return (
        <div>
            <center><h1>Wearhouse List</h1></center>
            {warehouses.map((warehouse) => (
                <div className="card">
                    <div className="card-body">
                        <h3 className="card-title">{warehouse.title}</h3>
                        <h5 className="card-title">Owner: {warehouse.owner}</h5>
                        <h6 className="card-subtitle mb-2 text-muted">Zone 1 temp: {warehouse.zone_1_temp}</h6>
                        <h6 className="card-subtitle mb-2 text-muted">Zone 2 temp: {warehouse.zone_2_temp}</h6>
                        <h6 className="card-subtitle mb-2 text-muted">Zone 3 temp: {warehouse.zone_3_temp}</h6>
                    </div>
                </div>
            ))}
        </div>
    )
};

export default Warehouses