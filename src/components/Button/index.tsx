import { ButtonContainer } from "./styles";
import { IButtonProps } from "./types";

const Button: React.FC<IButtonProps> = ({ title, onClick, disabled, style }: IButtonProps) => {
  return (
  <ButtonContainer onClick={onClick} disabled={disabled} style={style}>
      {title}
    </ButtonContainer>
  );
};

export default Button;
