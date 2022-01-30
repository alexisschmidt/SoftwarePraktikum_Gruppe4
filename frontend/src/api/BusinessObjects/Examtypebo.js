import NamedBo from "./NamedBo";

export default class ExamTypebo extends NamedBo {
  constructor() {
    super();
  }

  static fromJSON(examtype) {
    let result = [];

    if (Array.isArray(examtype)) {
      examtype.forEach((a) => {
        Object.setPrototypeOf(a, ExamTypebo.prototype);
        result.push(a);
      });
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let a = examtype;
      Object.setPrototypeOf(a, ExamTypebo.prototype);
      result.push(a);
    }

    return result;
  }
}
