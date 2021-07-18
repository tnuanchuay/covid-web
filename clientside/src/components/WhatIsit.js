import React from 'react';
import { Row, Col } from 'react-bootstrap';

export const WhatIsIt = () => {
    return (
        <Row id="#whatisit" className="justify-content-md-center">
            <Col md="auto">
                <p></p>
                <div>
                    <h2>Thailand Covid-19 cumulative cases forecasting [Unofficial!!]</h2>
                </div>
                <p>
                    COVID-19 Cumulative case forecasting using Neural Network with Gated Recurrent Unit(GRU).
                    GRU has a ability to forecast any time series dataset, With Back propagation through time (BPTT) technique.
                    GRU cells recieve processed information from previous cell and pass to next cell and 
                    also send feedback backward to previous cell during model training.
                </p>
                <p>
                    This experiment using available dataset from <a href="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv">github.com/owid/covid-19-data </a> 
                    which contain many features that can be used e.g., cumulative case, new case and vaccination.
                    the research selected cumulative case and vaccination from 90+ countries for trainning this machine learning model.

                </p>
            </Col>
        </Row>
    )
}