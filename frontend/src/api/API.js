import Modulebo from "./BusinessObjects/Modulebo";
import Modulepartbo from "./BusinessObjects/Modulepartbo";
import Personbo from "./BusinessObjects/Personbo";
import Semesterbo from "./BusinessObjects/Semesterbo";
import Spobo from "./BusinessObjects/Spobo";
import StudyCoursebo from "./BusinessObjects/StudyCoursebo";
import Userbo from "./BusinessObjects/Userbo";





export default class API {
  //Singleton instance
  static #api = null;

  //local Python backend
  #serverBaseURL = "/sopra";


  /* Routen aus dem Backend
Map([<Rule '/sopra/studycourses' (OPTIONS, POST, HEAD, GET, PUT) -> sopra_studycourse_list_operations>,
 <Rule '/sopra/moduleparts' (OPTIONS, POST, HEAD, GET, DELETE, PUT) -> sopra_module_part_list_operations>,
 <Rule '/sopra/semesters' (OPTIONS, HEAD, GET, POST) -> sopra_semester_list_operations>,
 <Rule '/sopra/spo-copy' (OPTIONS, PUT, DELETE, POST) -> sopra_spo_copy_operations>,
 <Rule '/sopra/modules' (OPTIONS, POST, HEAD, GET, DELETE, PUT) -> sopra_module_list_operations>,
 <Rule '/sopra/persons' (OPTIONS, POST, HEAD, GET, PUT) -> sopra_person_list_operations>,
 <Rule '/sopra/users' (OPTIONS, POST, HEAD, GET, PUT) -> sopra_user_list_operations>,
 <Rule '/sopra/spos' (OPTIONS, POST, HEAD, GET, PUT) -> sopra_spo_list_operations>,
 <Rule '/sopra/module/hash/<module_hash>' (OPTIONS, DELETE, HEAD, GET) -> sopra_module_hash_operations_2>,
 <Rule '/sopra/module/spo/<spo_hash>' (OPTIONS, HEAD, GET) -> sopra_module_spo_operations>,
 <Rule '/sopra/spo/hash/<spo_hash>' (OPTIONS, DELETE, HEAD, GET) -> sopra_spo_operations>,
 <Rule '/sopra/spo-by-startsemester-and-studycourse/<semester_hash>/<studycourse_hash>' (OPTIONS, HEAD, GET) -> sopra_spo_sem_stud_operations>,
 <Rule '/sopra/users-by-name/<lastname>' (OPTIONS, HEAD, GET) -> sopra_user_by_name_operations>,
 <Rule '/sopra/moduleparts/<modulepart_hash>' (OPTIONS, HEAD, GET) -> sopra_module_part_operations>,
 <Rule '/sopra/studycourse/<studycourse_hash>' (OPTIONS, HEAD, GET) -> sopra_module_part_operations_2>,
 <Rule '/sopra/studycourse/<studycourse_hash>' (OPTIONS, HEAD, GET, DELETE, PUT) -> sopra_module_part_operations_4>,
 <Rule '/sopra/person/<person_hash>' (OPTIONS, DELETE, HEAD, GET) -> sopra_module_part_operations_3>,
 <Rule '/sopra/user/<user_hash>' (OPTIONS, DELETE, HEAD, GET) -> sopra_module_hash_operations>]) */

  //definieren aller Urls für den Zugriff auf das Backend
  #getAllStudyCoursesUrl = () => { return this.#serverBaseURL + "/studycourses" };
  #getAllModulePartsUrl = () => { return this.#serverBaseURL + "/moduleparts"; }
  #getAllSemesterUrl = () => { return this.#serverBaseURL + "/semesters"; }
  #getAllSpoCopyUrl = () => { return this.#serverBaseURL + "/spo-copy"; }
  #getAllModulesURL = () => { return this.#serverBaseURL + "/modules"; }
  #getAllPersonsUrl = () => { return this.#serverBaseURL + "/persons"; }
  #getAllUsersUrl = () => { return this.#serverBaseURL + "/users"; }
  #getAllSposUrl = () => { return this.#serverBaseURL + "/spos"; }
  #getModuleByHashUrl = (moduleHash) => { return this.#serverBaseURL + "/module/hash/" + moduleHash; }
  #getModulesForSpoUrl = (spoHash) => { return this.#serverBaseURL + "/module/spo/" + spoHash; }
  #getSpoByStartsemesterAndStudycourseUrl = (semesterHash, studycourseHash) => { return this.#serverBaseURL + "/spo-by-startsemester-and-studycourse/" + semesterHash + "/" + studycourseHash; }
  #getUsersByNameUrl = (lastname) => { return this.#serverBaseURL + "/users-by-name/" + lastname; }
  #getModulePartsByHashUrl = (hash) => { return this.#serverBaseURL + "/moduleparts/" + hash; }
  #getStudyCourseByHashId = (hash) => { return this.#serverBaseURL + "/studycourse/" + hash; }
  #getPersonByHashUrl = (hash) => { return this.#serverBaseURL + "/person/" + hash; }
  #getUserByHashUrl = (userHash) => { return this.#serverBaseURL + "/user/" + userHash; }
  #getSpoByHashUrl = (hash) => {return this.#serverBaseURL + "/spo/" + hash};
  #getSemesterByHashUrl = (hash) => {return this.#serverBaseURL + "/semester" + hash};
  #getInfos =(hash) => {return this.#serverBaseURL + "/Infos" + hash};
  #getAllSpoRelatedURL = (id) => `${this.#serverBaseURL}/spos/studycourse/${id}`;



  /**
   * Get the Singelton instance
   *
   * @public
   */
  static getAPI() {
    if (this.#api == null) {
      this.#api = new API();
    }
    return this.#api;
  }

  #fetchAdvanced = (url, init) =>
    fetch(url, init).then((res) => {
      // The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500.
      if (!res.ok) {
        throw Error(`${res.status} ${res.statusText}`);
      }
      return res.json();
    });

    //Methoden für Zugriff auf das Backend
    //GET
    getAllModuleParts = () => {
      return this.#getAll(this.#getAllModulePartsUrl(), Modulepartbo);
    }
    addModulePart = (modulepart) => {
      return this.#add(this.#getAllModulePartsUrl(), modulepart, Modulepartbo);
    }
    updateModulePart = (modulepart) => {
      return this.#update(this.#getAllModulePartsUrl(), modulepart, Modulepartbo);
    }
    deleteModulePart = (modulepart) => {
      return this.#delete(this.#getAllModulePartsUrl(), modulepart, Modulepartbo);
    }
    getAllStudyCourses = () => {
      return this.#getAll(this.#getAllStudyCoursesUrl(), StudyCoursebo);
    }
    addStudyCourse = (studycourse) => {
      return this.#add(this.#getAllStudyCoursesUrl(), studycourse, StudyCoursebo);
    }
    updateStudyCourse = (studycourse) => {
      return this.#update(this.#getAllStudyCoursesUrl(), studycourse, StudyCoursebo);
    }
    deleteStudyCourse = (studycourse) => {
      return this.#delete(this.#getAllStudyCoursesUrl(), studycourse, StudyCoursebo);
    }
    getAllSemesters = () => {
      return this.#getAll(this.#getAllSemesterUrl(), Semesterbo);
    }
    addSemester = (semester) => {
      return this.#add(this.#getAllSemesterUrl(), semester, Semesterbo);
    }
    updateSemester = (semester) => {
      return this.#update(this.#getAllSemesterUrl(), semester, Semesterbo);
    }
    deleteSemester = (semester) => {
      return this.#delete(this.#getAllSemesterUrl(), semester, Semesterbo);
    }
    getAllModules = () => {
      return this.#getAll(this.#getAllModulesURL(), Modulebo);
    }
    addModule = (module) => {
      return this.#add(this.#getAllModulesURL(), module, Modulebo);
    }
    updateModule = (module) => {
      return this.#update(this.#getAllModulesURL(), module, Modulebo);
    }
    deleteModule = (module) => {
      return this.#delete(this.#getAllModulesURL(), module, Modulebo);
    }
    getAllPersons = () => {
      return this.#getAll(this.#getAllPersonsUrl(), Personbo);
    }
    addPerson = (person) => {
      return this.#add(this.#getAllPersonsUrl(), person, Personbo);
    }
    updatePerson = (person) => {
      return this.#update(this.#getAllPersonsUrl(), person, Personbo);
    }
    deletePerson = (person) => {
      return this.#delete(this.#getAllPersonsUrl(), person, Personbo);
    }
    getAllUsers = () => {
      return this.#getAll(this.#getAllUsersUrl(), Userbo);
    }
    addUser = (user) => {
      return this.#add(this.#getAllUsersUrl(), user, Userbo);
    }
    updateUser = (user) => {
      return this.#update(this.#getAllUsersUrl(), user, Userbo);
    }
    deleteUser = (user) => {
      return this.#delete(this.#getAllUsersUrl(), user, Userbo);
    }
    getAllSpos = () => {
      return this.#getAll(this.#getAllSposUrl(), Spobo);
    }
    addSpo = (spo) => {
      return this.#add(this.#getAllSposUrl(), spo, Spobo);
    }
    updateSpo = (spo) => {
      return this.#update(this.#getAllSposUrl(), spo, Spobo);
    }
    deleteSpo = (spo) => {
      return this.#delete(this.#getAllSposUrl(), spo, Spobo);
    }
    getModule = (hash) => {
      return this.#getSingle(this.#getModuleByHashUrl(hash), Modulebo);
    }
    getModuleParts = (hash) => {
      return this.#getSingle(this.#getModulePartsByHashUrl(hash), Modulepartbo);
    }
    getStudyCourse = (hash) => {
      return this.#getSingle(this.#getStudyCourseByHashId(hash), StudyCoursebo);
    }
    getPerson = (hash) => {
      return this.#getSingle(this.#getPersonByHashUrl(hash), Personbo);
    }
    getUser = (hash) => {
      return this.#getSingle(this.#getUserByHashUrl(hash), Userbo);
    }
    getSpo = (hash) => {
      return this.#getSingle(this.#getSpoByHashUrl(hash), Spobo);
    }
    getSemester = (hash) => {
      return this.#getSingle(this.#getSemesterByHashUrl(hash), Semesterbo);
    }
    getAllSpos = () => {
      return this.#getAll(this.#getAllSposUrl(), Spobo);
    }
    getAllModules = () => {
      return this.#getAll(this.#getAllModulesURL(), Modulebo);
    }
    getAllPersons = () => {
      return this.#getAll(this.#getAllPersonsUrl(), Personbo);
    }
    getAllUsers = () => {
      return this.#getAll(this.#getAllUsersUrl(), Userbo);
    }
    getAllSemesters = () => {
      return this.#getAll(this.#getAllSemesterUrl(), Semesterbo);
    }
    getAllStudyCourses = () => {
      return this.#getAll(this.#getAllStudyCoursesUrl(), StudyCoursebo);
    }
    getAllModulesParts = () => {
      return this.#getAll(this.#getAllModulePartsUrl(), Modulepartbo);
    }
    getInfos = () => {
      return this.#getAll(this.#getInfos(), Spobo);
      
    }

    async getAllSpoRelated(studyCourseId) {
			return this.#fetchAdvanced(this.#getAllSpoRelatedURL(studyCourseId));
		}

       



  


    #getSingle = (url,BO) => {
      return this.#fetchAdvanced(url).then( responseJSON => {
          let responseBO = BO.fromJSON(responseJSON)[0];
          return new Promise(function(resolve){
              resolve(responseBO);
          })
      })
  }
  #getAll = (url, BO) => {
      return this.#fetchAdvanced(url).then((responseJSON) => {
          let responseBOs = BO.fromJSON(responseJSON);
          return new Promise(function (resolve) {
              resolve(responseBOs);
          })
      })
  } 
  #delete = (url, BO) => {
      return this.#fetchAdvanced(url, {
          method: 'DELETE'
      }).then((responseJSON) => {
          let responseBO = BO.fromJSON(responseJSON)[0];
          return new Promise(function (resolve) {
              resolve(responseBO);
          })
      })
  }

  #update = (url, businessObject, BO)=>{
      return this.#fetchAdvanced(url, {
          method: 'PUT',
          headers: {
              'Accept': 'application/json, text/plain',
              'Content-type': 'application/json',
          },
          body: JSON.stringify(businessObject)
          }).then((responseJSON) => {
          let responseBO = BO.fromJSON(responseJSON)[0];
          return new Promise(function (resolve) {
              resolve(responseBO);
          })
      })
  }
  #add = (url,businessObject, BO) =>{
      return this.#fetchAdvanced(url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json, text/plain',
          'Content-type': 'application/json',
        },
        body: JSON.stringify(businessObject)
      }).then((responseJSON) => {
        let responseBO = BO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(responseBO);
        })
      })
  }
}
