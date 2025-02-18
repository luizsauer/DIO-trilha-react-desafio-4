export interface IFormLogin {
    email: string;
    password: string;
    disabled?: boolean;
    onClick?: () => void;
}

export const defaultValues: IFormLogin = {
    email: '',
    password: ''
}