import Businessobject from './Businessobject';

export default class NamedBo extends Businessobject{
  
   constructor() {
    super();
    this.name=''
    this.title=''

  }

setName(name){
    this.name=name
    
}

setTitle(title){
    this.title=title
}

getName(){
    return this.name
}

getTitle(){
    return this.title
}

}