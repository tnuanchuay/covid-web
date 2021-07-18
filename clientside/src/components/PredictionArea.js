import React, { useState, useEffect } from 'react';
import { AreaChart, XAxis, YAxis, CartesianGrid, Area, Tooltip, ResponsiveContainer } from 'recharts';
import mock from './mockdata.json';

export const PredictionArea = () => {

    const [data, setdata] = useState(0);

    useEffect(() => {
        fetch("http://localhost:5000/data")
            .then(res => res.json())
            .then(
                json => {
                    setdata(json);
                },
                err => {
                    alert(err);
                })
    }, []);

    return (
        <ResponsiveContainer width="100%" height={500}>
            <AreaChart  height="100%" width={500} data={data.data} margin={{ top: 20, right: 30, left: 0, bottom: 0 }}>
                <XAxis dataKey="date" />
                <YAxis />
                <CartesianGrid strokeDasharray="3 3" />
                <Tooltip />
                <Area type="monotone" dataKey="cases" stroke="#FF0000" fillOpacity={1} fill="url(#colorUv)" />
                <Area dataKey="prediction" stroke="#FF0000" fill="#FF0000" />
            </AreaChart>
        </ResponsiveContainer>
    );
}