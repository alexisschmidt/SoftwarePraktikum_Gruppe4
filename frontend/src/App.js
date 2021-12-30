import React from 'react';
import { BrowserRouter as Router, Navigate, Redirect } from 'react-router-dom';
import { Container, ThemeProvider, CssBaseline } from '@material-ui/core'; //um Material-UI-Komponente nutzen zu können
import firebase from 'firebase/app';
import Header from './components/layout/Header';
import 'firebase/auth';
import Theme from './Theme';
import firebaseConfig from './firebaseconfig';
import SignIn from './components/pages/SignIn';
import LoadingProgress from './components/dialogs/LoadingProgress';
import ContextErrorMessage from './components/dialogs/ContextErrorMessage';


class App extends React.Component {

	/** Konstrukteur der App, Firebase initialisiert */
	constructor(props) {
		super(props);

		// Init einen leeren Zustand
		this.state = {
			currentUser: null,
			appError: null,
			authError: null,
			authLoading: false
		};
	}

	/**Erstellen Sie eine Fehlergrenze für diese App und erhalten Sie alle Fehler unterhalb des Komponentenbaums*/

   static getDerivedStateFromError(error) {
		// Aktualisieren Sie den Status, damit beim nächsten Rendering die Fallback-Benutzeroberfläche angezeigt wird.
		return { appError: error };
	}

	/** Verarbeitet Firebase-Benutzer, die bei Statusänderungen angemeldet sind  */
	handleAuthStateChange = user => {
		if (user) {
			this.setState({
				authLoading: true
			});
			// Der Benutzer ist angemeldet
			user.getIdToken().then(token => {
			// Die Token werden zu den Cookies im Browser hinzugefügt. Der Server kann dann schließlich das Token anhand der API verifizieren.

				document.cookie = `token=${token};path=/`;

				// Setzen Sie den Benutzer nicht, bevor der Token angekommen ist
				this.setState({
					currentUser: user,
					authError: null,
					authLoading: false
				});
			}).catch(e => {
				this.setState({
					authError: e,
					authLoading: false
				});
			});
		} else {
			// Der Benutzer hat sich abgemeldet --> löschen der ID-Token

			document.cookie = 'token=;path=/';

			// Abgemeldeter Benutzer auf null setzen
			this.setState({
				currentUser: null,
				authLoading: false
			});
		}
	}



 handleSignIn = () => {
  this.setState({
    authLoading: true
  });
  const provider = new firebase.auth.GoogleAuthProvider();
  firebase.auth().signInWithRedirect(provider);
}

/**
 * Lifecycle-Methode, die aufgerufen wird, wenn die Komponente in das DOM des Browsers eingefügt wird.
 * Initialisiert das Firebase SDK.
 */
componentDidMount() {
  firebase.initializeApp(firebaseConfig);
  firebase.auth().languageCode = 'en';
  firebase.auth().onAuthStateChanged(this.handleAuthStateChange);
}



/** Die gesamte App wird gerendert */
render() {
  const { currentUser, appError, authError, authLoading } = this.state;

  return (
    <ThemeProvider theme={Theme}>
      {/* 
Globales CSS-Reset und Browser-Normalisierung. CssBaseline startet eine elegante, konsistente und einfache Baseline, auf der aufgebaut werden kann. */}
      <CssBaseline />
      <Router basename={process.env.PUBLIC_URL}>
        <Container maxWidth='md'>
          <Header user={currentUser} />
		  {
							// Is a user signed in?
							currentUser ?
								<>
								</>
								:
								// else show the sign in page
								<>

									<SignIn onSignIn={this.handleSignIn} />
								</>
						}
						<LoadingProgress show={authLoading} />
						<ContextErrorMessage error={authError} contextErrorMsg={`Something went wrong during sighn in process.`} onReload={this.handleSignIn} />
						<ContextErrorMessage error={appError} contextErrorMsg={`Something went wrong inside the app. Please reload the page.`} />
        </Container>
      </Router>
    </ThemeProvider>
  );
}
}

export default App;
