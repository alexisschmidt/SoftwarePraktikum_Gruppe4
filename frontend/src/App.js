import React from 'react';
import Studentview from "./components/pages/Studentview";
import SpoStudent from "./components/pages/SpoStudent";

/* import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import { Container, ThemeProvider, CssBaseline } from '@material-ui/core';
import firebase from 'firebase/app';
import 'firebase/auth';
import SignIn from './Components/Pages/SignIn';
import firebaseConfig from './firebaseConfig';
import ContextErrorMessage from "./Components/Dialog/ContextErrorMessage"; */




/**
 * 
 * Die einzelnen Komponente werden hier aufgerufen.
 * Dadurch können wir sie auf der Webseite anzeigen lassen.
 * 
 * @author [Sarah Rowan](https://github.com/sr168)
 */


 class App extends React.Component {

	constructor(props) {
		super(props);

		// Init an empty state
		this.state = {
			currentUser: null,
			appError: null,
			authError: null,
			authLoading: false,
			googleId: null,
		};
	}



	render(){
		return (
		<div>
		<Studentview />
		<SpoStudent />
		
		</div>
	);
	}
 }
export default App;
