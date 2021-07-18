import React from "react";
import { Container, Row, Col } from "react-bootstrap";

import { Header } from './Header'
import { PredictionArea } from "./PredictionArea";
import { WhatIsIt } from "./WhatIsit";
export const Layout = () => {
    return (
        <main>
            <Header></Header>
            <Container>
                <Row>
                    <Col>
                        <PredictionArea></PredictionArea>
                    </Col>
                </Row>
                <Row></Row>
                <Row>
                    <Col>
                        <WhatIsIt></WhatIsIt>
                    </Col>
                </Row>
            </Container>
        </main>
    )
}