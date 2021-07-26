import React from 'react';
import { Row, Col, Image } from 'react-bootstrap';

export const WhatIsIt = () => {
    return (
        <div>
            <Row id="#whatisit" className="justify-content-md-center">
                <Col md="auto">
                    <p></p>
                    <div>
                        <h2>Thailand Covid-19 cumulative cases forecasting [Unofficial!!][Untrustable!!]</h2>
                    </div>
                    <p>
                        COVID-19 Cumulative case forecasting using Neural Network with Gated Recurrent Unit(GRU).
                        GRU has a ability to forecast any time series dataset. Mostly this technique is used for NLP and Regression problem.
                        With Back propagation through time (BPTT) technique, GRU cells recieve processed information from previous cell and pass to next cell and
                        also send feedback backward to previous cell during model training.
                    </p>
                    <p>
                        This experiment use available dataset from <a href="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv">github.com/owid/covid-19-data </a>
                        which contain many features that can be used e.g., cumulative case, new case and vaccination.
                        The researcher selected number of cumulative case and vaccination from 90+ countries for trainning and validate this machine learning model.
                        Train the ML model with 50 day of [Cumulative case, Vaccination total] blocks. Use Adam optimizer, MAE as a loss function, MAPE as a indicator.
                        Each models return cumulative case on next 7, 14, 21, 28 day ahead.
                    </p>
                    <p>

                    </p>
                </Col>
            </Row>
            <Row md="auto">
                <Col xs={4} md={4}></Col>
                <Col xs={4} md={4}>
                    <Image className="justify-content-md-center" src="https://raw.githubusercontent.com/tspn/covid-web/main/Screen%20Shot%202564-07-18%20at%2022.43.15.png" width="100%" height="100%"></Image>
                </Col>
                <Col xs={4} md={4}></Col>
            </Row>
            <Row>
                <Col md="auto">
                    <p>
                        DISCLAIMER !!!
                        Results from this experiment is not accurate at all. This experiment is another part of my learning (machine learning).
                        Do not use this as a reference for COVID-19 forecasting.
                    </p>
                </Col>
            </Row>
        </div>
    )
}