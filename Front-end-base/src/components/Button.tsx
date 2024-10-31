const Input = ({
    id,
  classes,
  type,
}: {
  id: string;
  classes: string;
  type: string;
}) => {
  return <input type={type} className={classes} id={id}/>;
};

const Button = ({ text, classes, }: { text: string; classes: string; }) => {
  return <button className={classes}>{text} </button>;
};

export { Input, Button };
