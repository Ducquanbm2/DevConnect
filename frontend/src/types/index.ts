export type UserRole = "USER" | "ADMIN";
export type ArticleStatus = "DRAFT" | "PUBLISHED";

export interface User {
  id: number;
  email: string;
  username: string;
  full_name?: string | null;
  bio?: string | null;
  avatar_url?: string | null;
  role: UserRole;
  created_at: string;
}

export interface Tag {
  id: number;
  name: string;
  slug: string;
  color_hex: string;
  description?: string | null;
}

export interface ArticleSummary {
  id: number;
  title: string;
  slug: string;
  summary?: string | null;
  cover_image_url?: string | null;
  status: ArticleStatus;
  view_count: number;
  vote_score: number;
  published_at?: string | null;
  author: Pick<User, "id" | "username" | "full_name" | "avatar_url">;
  tags: Tag[];
}

export interface PaginationMeta {
  page: number;
  page_size: number;
  total_items: number;
  total_pages: number;
}

export interface ApiResponse<T> {
  success: boolean;
  message?: string;
  data: T;
}

export interface PaginatedResponse<T> {
  success: boolean;
  data: T[];
  meta: PaginationMeta;
}

export interface ApiErrorResponse {
  success: false;
  error: {
    code: string;
    message: string;
    details?: unknown;
  };
}
