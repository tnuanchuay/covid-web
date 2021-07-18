import React from "react";
import { Navbar, Nav, NavDropdown, Container } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

export const Header = () => {
    return (
        <Navbar bg="light" expand="lg">
            <Container>
                <Navbar.Brand href="#">Forecasting COVID-19 daily - Thailand</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <NavDropdown.Item href="#whatisit">What is it ?</NavDropdown.Item>
                        <NavDropdown.Item href="https://github.com/tspn">About me</NavDropdown.Item>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}