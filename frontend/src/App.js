import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
//import PrivateRoute from './Privateroute'
import { Container, ThemeProvider, CssBaseline } from "@material-ui/core"; //um Material-UI-Komponente nutzen zu können
import firebase from "firebase/app";
import Header from "./components/layout/Header";
import "firebase/auth";
import Theme from "./Theme";
import firebaseConfig from "./firebaseconfig";
import SignIn from "./components/pages/SignIn";
import LoadingProgress from "./components/dialogs/LoadingProgress";
import ContextErrorMessage from "./components/dialogs/ContextErrorMessage";
//import SpoStudent from "./components/pages/SpoStudent";
import About from "./components/pages/About";
//import Admin from "./components/pages/AdminSpoAnsicht";
//import Spoliste from './components/pages/Spoliste';
//import StudyCourses from './components/pages/StudyCourses';
import AllStudyCourses from './components/AllStudycourses';
// import SpoAuswählenOMM from './components/pages/SpOAuswählenOMM';
//import Spowi from './components/pages/Spowi';
//import SpoStudyCoursesList from './components/SpoStudyCoursesList';
//import AdminSpoAnsicht from './components/AdminSpoAnsicht';
//import AdminSpoEdit from './components/AdminSpoEdit';
import AdminTable from './components/content/AdminTable';
//import AdminStudiengangAuswahl from "./components/pages/AdminStudiengangAuswahl";
//import SpoForm from "./components/pages/SpoForm";
import Administration from "./components/pages/SpoManagement";
import SpoUeberblick from "./components/pages/SpoUeberblick";


class App extends React.Component {
  /** Konstrukteur der App, Firebase initialisiert */
  constructor(props) {
    super(props);

    // Init einen leeren Zustand
    this.state = {
      currentUser: null,
      appError: null,
      authError: null,
      authLoading: false,
    };
  }

  /**Erstellen Sie eine Fehlergrenze für diese App und erhalten Sie alle Fehler unterhalb des Komponentenbaums*/

  static getDerivedStateFromError(error) {
    // Aktualisieren Sie den Status, damit beim nächsten Rendering die Fallback-Benutzeroberfläche angezeigt wird.
    return { appError: error };
  }

  /** Verarbeitet Firebase-Benutzer, die bei Statusänderungen angemeldet sind  */
  handleAuthStateChange = (user) => {
    if (user) {
      this.setState({
        authLoading: true,
      });
      // Der Benutzer ist angemeldet
      user
        .getIdToken()
        .then((token) => {
          // Die Token werden zu den Cookies im Browser hinzugefügt. Der Server kann dann schließlich das Token anhand der API verifizieren.

          document.cookie = `token=${token};path=/`;

          // Setzen Sie den Benutzer nicht, bevor der Token angekommen ist
          this.setState({
            currentUser: user,
            authError: null,
            authLoading: false,
          });
        })
        .catch((e) => {
          this.setState({
            authError: e,
            authLoading: false,
          });
        });
    } else {
      // Der Benutzer hat sich abgemeldet --> löschen der ID-Token

      document.cookie = "token=;path=/";

      // Abgemeldeter Benutzer auf null setzen
      this.setState({
        currentUser: null,
        authLoading: false,
      });
    }
  };

  handleSignIn = () => {
    this.setState({
      authLoading: true,
    });
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithRedirect(provider);
  };

  /**
   * Lifecycle-Methode, die aufgerufen wird, wenn die Komponente in das DOM des Browsers eingefügt wird.
   * Initialisiert das Firebase SDK.
   */
  componentDidMount() {
    firebase.initializeApp(firebaseConfig);
    firebase.auth().languageCode = "en";
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
									<Route path="/" exact component={About} />
									{/* <Route path="/Studiengangauswahl" exact component={StudyCourses}/> */}
									<Route path="/admin" exact component={AllStudyCourses}/>
									<Route path="/admintable" exact component={AdminTable}/>
									{/* <Route path="/admin/:studyCourseID" exact component={SpoStudyCoursesList}/>
									<Route path="/admin/:studyCourseID/:spoID" exact component={AdminSpoAnsicht}/>
									<Route path="/adminspoedit" exact component={AdminSpoEdit}/> */}
									{/* <Route path="/admin/:spoID/spoansicht" exact component={AdminSpoAnsicht}/> */}
									{/*<Route path="/spoansicht" exact component={AdminSpoAnsicht}/>*/}
									{/* <Route path="/Spoauswahl2" exact comonent={SpoAuswählenOMM}/> */}
								{/* 	<Route path="/Spoauswahl" exact comonent={Spowi}/>
                  <Route path="/SpoForm" exact component={SpoForm} /> */}
									{/*<Route path="/Altespo" exact component ={}/>*/}
									{/* <Route path="/Spoerstellen" exact component={Admin}/> */}
									{/* <Route path="/Spo" exact component={SpoStudent}/> */}
                  <Route path="/Administration"
                    exact
                    component={Administration}
                  />
                  {/*  <Route path="/Spoauswahl" exact component={Spowi} />
                   <Route
                    path="/AdminStudiengangAuswahl"
                    exact
                    component={AdminStudiengangAuswahl}
                  />
                  <Route path="/Spoauswahl" exact component={Spowi} /> */}
								</>
								:
								// else show the sign in page
								<>
								
							{/* 	<Route path="/student">
									<SpoStudent />
									</Route> */}

									<SignIn onSignIn={this.handleSignIn} />
								</>
						}
						<LoadingProgress show={authLoading} />
						<ContextErrorMessage error={authError} contextErrorMsg={`Something went wrong during sighn in process.`} onReload={this.handleSignIn} />
						<ContextErrorMessage error={appError} contextErrorMsg={`Something went wrong inside the app. Please reload the page.`} />
						{/* <List/> */}
						{/* <DateAndTime/> */}
	    </Container>
      </Router>
    </ThemeProvider>
  );
}
}

export default App;
